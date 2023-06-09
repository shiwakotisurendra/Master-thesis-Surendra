// https://leaflet-extras.github.io/leaflet-providers/preview/
      // var osm = L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
      //   maxZoom: 19,
      //   attribution: "© OpenStreetMap",
      // });

      // var streets = L.tileLayer(mapboxUrl, {
      //   id: "mapbox/streets-v11",
      //   tileSize: 512,
      //   zoomOffset: -1,
      //   attribution: '&copy mapboxAttribution',
      // });

      // var map = L.map("map", {
      //   center: [39.73, -104.99],
      //   zoom: 10,
      //   layers: [osm, cities],
      // });

      // var baseMaps = {
      //   OpenStreetMap: osm,
      //   "Mapbox Streets": streets,
      // };
      const mapboxUrl =
        "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw";
      var map = L.map("map").setView([51.505, -0.09], 13);

      var osm = L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution: "© OpenStreetMap",
      });

      var streets = L.tileLayer(mapboxUrl, {
        id: "mapbox/streets-v11",
        tileSize: 512,
        zoomOffset: -1,
        attribution: "&copy mapboxAttribution",
      });

      var OpenTopoMap = L.tileLayer(
        "https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png",
        {
          maxZoom: 17,
          attribution:
            'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)',
        }
      );

      var StadiaDark = L.tileLayer(
        "https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png",
        {
          maxZoom: 20,
          attribution:
            '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
        }
      );

      var StamenToner = L.tileLayer(
        "https://stamen-tiles-{s}.a.ssl.fastly.net/toner/{z}/{x}/{y}{r}.{ext}",
        {
          attribution:
            'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
          subdomains: "abcd",
          minZoom: 0,
          maxZoom: 20,
          ext: "png",
        }
      );

      var Stamen_Terrain = L.tileLayer(
        "https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}{r}.{ext}",
        {
          attribution:
            'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
          subdomains: "abcd",
          minZoom: 0,
          maxZoom: 18,
          ext: "png",
        }
      );

      var EsriWorldImagery = L.tileLayer(
        "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
        {
          attribution:
            "Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community",
        }
      );

      var Esri_NatGeoWorldMap = L.tileLayer(
        "https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}",
        {
          attribution:
            "Tiles &copy; Esri &mdash; National Geographic, Esri, DeLorme, NAVTEQ, UNEP-WCMC, USGS, NASA, ESA, METI, NRCAN, GEBCO, NOAA, iPC",
          maxZoom: 16,
        }
      );

      var OpenSeaMap = L.tileLayer('http://tiles.openseamap.org/seamark/{z}/{x}/{y}.png',
                 name='OpenSeaMap',
                 attr='Map data © OpenSeaMap contributors').addTo(map)

      osm.addTo(map);
      var baseMaps = {
        OpenStreetMap: osm,
        "Mapbox Streets": streets,
        OpenTopoMap: OpenTopoMap,
        StadiaDarkMap: StadiaDark,
        StamenTonerMap: StamenToner,
        StamenTerrainMap: Stamen_Terrain, 
        EsriWorldImagery: EsriWorldImagery,
        EsriNatGeoWorldMap: Esri_NatGeoWorldMap,
  
      };

      var lControl = L.control.layers(baseMaps).addTo(map);
      // var tile = L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
      //   maxZoom: 19,
      //   attribution:
      //     '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
      // }).addTo(map);

      var marker = L.marker([51.5, -0.09]).addTo(map);

      var circle = L.circle([51.508, -0.11], {
        color: "red",
        fillColor: "#f03",
        fillOpacity: 0.5,
        radius: 500,
      }).addTo(map);

      var polygon = L.polygon([
        [51.509, -0.08],
        [51.503, -0.06],
        [51.51, -0.047],
      ]).addTo(map);

      var popup = L.popup()
        .setLatLng([51.513, -0.09])
        .setContent("I am a standalone popup.")
        .openOn(map);

      function onMapClick(e) {
        popup
          .setLatLng(e.latlng)
          .setContent("You clicked the map at " + e.latlng.toString())
          .openOn(map);
      }

      map.on("click", onMapClick);

      // var myLines = [
      //   {
      //     type: "LineString",
      //     coordinates: [
      //       [-100, 40],
      //       [-105, 45],
      //       [-110, 55],
      //     ],
      //   },
      //   {
      //     type: "LineString",
      //     coordinates: [
      //       [-105, 40],
      //       [-110, 45],
      //       [-115, 55],
      //     ],
      //   },
      // ];

      // var myStyle = {
      //   color: "#ff7800",
      //   weight: 5,
      //   opacity: 0.65,
      // };

      // L.geoJSON(myLines, {
      //   style: myStyle,
      // }).addTo(map);

      function onEachFeature(feature, layer) {
        // does this feature have a property named popupContent?
        if (feature.properties && feature.properties.popupContent) {
          layer.bindPopup(feature.properties.popupContent);
        }
      }

      var geojsonFeature = [
        {
          type: "Feature",
          properties: {
            name: "Coors Field",
            amenity: "Baseball Stadium",
            popupContent: "This is where the Rockies play!",
          },
          geometry: {
            type: "Point",
            coordinates: [-104.99404, 39.75621],
          },
        },
        {
          type: "Feature",
          properties: {
            name: "Coors Field",
            amenity: "Baseball Stadium",
            popupContent: "This is where the Rockies play!",
          },
          geometry: {
            type: "LineString",
            coordinates: [
              [-105, 40],
              [-110, 45],
              [-115, 55],
            ],
          },
        },
      ];

      L.geoJSON(geojsonFeature, {
        onEachFeature: onEachFeature,
      }).addTo(map);

      var someFeatures = [
        {
          type: "Feature",
          properties: {
            name: "Coors Field",
            show_on_map: true,
            popupContent: "This is where surendra play",
          },
          geometry: {
            type: "Point",
            coordinates: [-104.99404, 39.78],
          },
        },
        {
          type: "Feature",
          properties: {
            name: "Busch Field",
            show_on_map: true,
            popupContent: "This is where surendra play",
          },
          geometry: {
            type: "Point",
            coordinates: [-104.98404, 39.74621],
          },
        },
      ];

      L.geoJSON(someFeatures, {
        filter: function (feature, layer) {
          return feature.properties.show_on_map;
        },
      }).addTo(map);

      var littleton = L.marker([39.61, -105.02]).bindPopup(
          "This is Littleton, CO."
        ),
        denver = L.marker([39.74, -104.99]).bindPopup("This is Denver, CO."),
        aurora = L.marker([39.73, -104.8]).bindPopup("This is Aurora, CO."),
        golden = L.marker([39.77, -105.23]).bindPopup("This is Golden, CO.");

      var cities = L.layerGroup([littleton, denver, aurora, golden]);
      var overlayMaps = {
        Cities: cities,
      };