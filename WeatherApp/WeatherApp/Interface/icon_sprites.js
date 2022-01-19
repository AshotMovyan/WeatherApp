ymaps.ready(init);

function init() {
    var erevan = "20°C";
    var vanadzor = "17°C";
    var myMap = new ymaps.Map("map", {
            center: [40.327977243850356, 44.57353844620169],
            zoom: 8
        }, {
            searchControlProvider: 'yandex#search'
        }),

    // Создаем геообъект с типом геометрии "Точка".a
        myGeoObject = new ymaps.GeoObject({
            // Description Geometry.
            
        }, {
            // Properties
            // Иконка метки будет растягиваться под размер ее содержимого.
            preset: 'islands#blackStretchyIcon',
            // Метку можно перемещать.
            draggable: true
        }),
        myPieChart = new ymaps.Placemark([
            41.980735348915466, 43.97393445809855
        ], {
            // Diagram datas
            data: [
                {weight: 8, color: '#0E4779'},
                {weight: 6, color: '#1E98FF'},
                {weight: 4, color: '#82CDFF'}
            ],
            iconCaption: erevan
        }, {
            // Зададим произвольный макет метки.
            iconLayout: 'default#pieChart',
            // Радиус диаграммы в пикселях.
            iconPieChartRadius: 30,
            // Радиус центральной части макета.
            iconPieChartCoreRadius: 10,
            // Стиль заливки центральной части.
            iconPieChartCoreFillStyle: '#ffffff',
            // Cтиль линий-разделителей секторов и внешней обводки диаграммы.
            iconPieChartStrokeStyle: '#ffffff',
            // Ширина линий-разделителей секторов и внешней обводки диаграммы.
            iconPieChartStrokeWidth: 3,
            //Marker Max width 
            iconPieChartCaptionMaxWidth: 200
        });

    myMap.geoObjects
        .add(myGeoObject)
        .add(myPieChart)
    
      
        .add(new ymaps.Placemark([40.13773865755883, 44.44085340763167], {
            balloonContent: "Text",
            iconCaption: erevan
        }, {
            preset: 'islands#circleIcon',
            iconColor: '#3caa3c'
        }))
      
       
        .add(new ymaps.Placemark([40.864518476113695, 43.85308488002371], {
            balloonContent: 'eli text',
            iconCaption: 'TEXT'
        }, {
            preset: 'islands#greenDotIconWithCaption'
        }))
        .add(new ymaps.Placemark([40.81505486516969, 44.49222856532953], {
            balloonContent: 'Vanadzor Batumi Street',
            iconCaption: vanadzor
        }, {
            preset: 'islands#blueCircleDotIconWithCaption',
            iconCaptionMaxWidth: '50'
        }));
}
