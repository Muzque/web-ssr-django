const vm = new Vue({
    delimiters: ['[[', ']]'],
    el : '#app',
    data : {
        playlist : [],
        videos : null
    },
    methods : {
        getPlaylist : function() {
            var self = this;
            var query = document.getElementById("query").value;
            var endpoint = '/youtube/api/playlist/';
            $.ajax({
                method: "GET",
                url: endpoint,
                data: {
                    query: query
                },
                success: function (data) {
                    // console.log(data);
                    self.playlist = data;
                },
                error: function (error_data) {
                    alert("失敗");
                    // console.log(error_data);
                }
            });
        },
        getListen : function(e) {
            e = e || window.event;
            e = e.target || e.srcElement;
            var self = this;
            var playlistId = e.id;
            var endpoint = '/youtube/api/listen/';
            $.ajax({
                method: "GET",
                url: endpoint,
                data: {
                    playlistId: playlistId
                },
                success: function (data) {
                    // console.log(data);
                    self.videos = data;
                },
                error: function (error_data) {
                    alert("失敗");
                    // console.log(error_data);
                }
            })
        }
    }
});