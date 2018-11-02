// 添加地图
var map = new AMap.Map("container", {
    resizeEnable: true,
    zoomEnable: true,
    center: [114.300917, 30.582882],
    zoom: 11
});

// 添加标尺
var scale = new AMap.Scale();
map.addControl(scale);

//经度，纬度，时间（用不到），通勤方式（默认是地铁＋公交）
var x, y, t, vehicle = "BUS";
//工作地点，工作标记
var workAddress, workMarker;
//房源标记队列
var makers = [];
var infowindowArray = [];
//多边形队列，存储公交到达的计算结果
var polygonArray = [];
//路径规划
var amapTransfer;


var auto = new AMap.Autocomplete({
    //通过id指定输入元素
    input: "work-location",
    city:'武汉'
});
//添加事件监听，在选择补完的地址后调用workLocationSelected
AMap.event.addListener(auto, "select", workLocationSelected);

// 乘坐公交
function takeBus(radio) {
    vehicle = radio.value;
    loadWorkLocation()
}

// 乘坐地铁
function takeSubway(radio) {
    vehicle = radio.value;
    loadWorkLocation()
}

// 工作地点选择
function workLocationSelected(e) {
    workAddress = e.poi.name;
    loadWorkLocation();
}

// 删除工作地点的标记和到达圈
function delWorkLocation() {
    // 如果多边形数组存在，则删除多边形数组
    if (polygonArray) map.remove(polygonArray);
    // 如果工作地点的标记存在，则删除工作地点标记
    if (workMarker) map.remove(workMarker);
    polygonArray = [];
}
// 载入工作地点的标记
function loadWorkMarker(x, y, locationName) {
    // 工作地点标记
    workMarker = new AMap.Marker({
        map: map,
        title: locationName,    // 鼠标滑过点标记时的文字提示，不设置则鼠标滑过点标无文字提示
        icon: 'http://webapi.amap.com/theme/v1.3/markers/n/mark_r.png',
        position: [x, y]     // 点标记在地图上显示的位置，默认为地图中心点

    });
}

// 载入工作地点到达圈
function loadWorkRange(x, y, t, color, vehicle) {
    // 创建一个工作地点到达圈对象
    var arrivalRange = new AMap.ArrivalRange();
    arrivalRange.search([x, y], t, function(status, result) {

        if (result.bounds) {
            for (var i = 0; i < result.bounds.length; i++) {
                var polygon = new AMap.Polygon({
                    map: map,
                    fillColor: color,
                    fillOpacity: "0.4",
                    strokeColor: color,
                    strokeOpacity: "0.8",
                    strokeWeight: 1
                });
                polygon.setPath(result.bounds[i]);
                polygonArray.push(polygon);
            }
        }
        $.get('http://127.0.0.1:5009/location_all',function(data){
            // console.log(data);
            var points = data.result;
            // console.log(points);
            for (i=0;i<points.length;i++){
                for (var n = 0;n<polygonArray.length;n++){
                    if(polygonArray[n].contains(points[i].address)){
                        var maker = new AMap.Marker({
                            position:points[i].address,
                            map:map,
                            icon:'http://webapi.amap.com/theme/v1.3/markers/n/mark_b.png'
                        });
                        maker.code = points[i].id;
                        maker.on('click', showInfo);
                        makers.push(maker)
                    }
                }
            }
        })
    }, {
        policy: vehicle
    });
}

// 1.把前面设置进marker的属性code的值拼接进url,
// 通过ajax请求数据,把数据传给打开信息窗体函数
function showInfo(e){
     url  = "http://127.0.0.1:5009/infor/" + e.target.code;
     $.get(url,function (dat) {
         data = dat;
         fopen(data,e);
     });
 }
// 2.自定义信息窗体,打开位置为,marker的位置,内容为createInfoWindow(data)的返回值
 function fopen(data,e) {
    var infoWindow2 = new AMap.InfoWindow({
    isCustom:true,  //使用自定义窗体
    // title:data.title1,
    content:createInfoWindow(data),
    size:new AMap.Size(300, 0),
    offset:new AMap.Pixel(107, -13)//-113, -140
    });
    infowindowArray.push(infoWindow2)
    infoWindow2.open(map,e.target.getPosition());
}

// 3.根据ajax的返回值,拼接信息窗体

function createInfoWindow(data) {
    var title = data.title1;
    var location1 = data.location1;
    var more_href= data.url1;
    var money= data.money;
    var info = document.createElement("div");
    info.className = "custom-info input-card content-window-card";

    //可以通过下面的方式修改自定义窗体的宽高
    // 定义顶部标题
    var title1 = title + '<span style="font-size:20px;color:#F00;">价格:' + String(money) + '</span>'
    var top = document.createElement("div");
    var titleD = document.createElement("div");
    var closeX = document.createElement("img");
    top.className = "info-top";
    top.style.backgroundColor = '#64a8f9'
    titleD.innerHTML = title1;
    closeX.src = "https://webapi.amap.com/images/close2.gif";
    closeX.onclick = closeInfoWindow;

    top.appendChild(titleD);
    top.appendChild(closeX);
    info.appendChild(top);

    // 定义中部内容
    var content = [];
    var loca = '小区：' + location1;
    content.push(loca);
    var more = "<a href='" + more_href + "' target='_blank'>详细信息</a>";
    content.push(more)
    var middle = document.createElement("div");
    middle.className = "info-middle";
    middle.style.backgroundColor = 'white';
    middle.innerHTML = content.join("<br/>");
    info.appendChild(middle);

    // 定义底部内容
    var bottom = document.createElement("div");
    bottom.className = "info-bottom";
    bottom.style.position = 'relative';
    bottom.style.top = '0px';
    bottom.style.margin = '0 auto';
    var sharp = document.createElement("img");
    sharp.src = "https://webapi.amap.com/images/sharp.png";
    bottom.appendChild(sharp);
    info.appendChild(bottom);
    return info;
}

// 4.为信息窗体的x图标添加点击事件,关闭信息窗
function closeInfoWindow(){
    infowindowArray = []
    map.clearInfoWindow();
}

// 载入工作地点
function loadWorkLocation() {
    delWorkLocation();
    delRentLocationMarkers()
    var geocoder = new AMap.Geocoder({
        city: "武汉",
        radius: 1000   //逆地理编码时，以给定坐标为中心点，单位：米
                        // 取值范围：0-3000
                        // 默认值：1000
    });
    // 工作地点的正向地理编码获得坐标的值
    geocoder.getLocation(workAddress, function(status, result) {
        // 高德API的示例写法

        if (status === "complete" && result.info === 'OK') {
            // 当status为complete时，result为GeocodeResult；
            // result中对应详细地理坐标信息
            var geocode = result.geocodes[0];
            // 经度
            x = geocode.location.getLng();
            // 纬度
            y = geocode.location.getLat();
            // 工作地点标记
            loadWorkMarker(x, y);
            // 工作地点到达圈的多边形
            // console.log(vehicle);
            loadWorkRange(x, y, 60, "#3f67a5", vehicle);
            // 设置地图的缩放等级和中心
            map.setZoomAndCenter(12, [x, y]);
        }
    })
}

function delRentLocationMarkers() {
    if (makers) map.remove(makers);
    if (infowindowArray) map.clearInfoWindow();
}

