const vm = new Vue({
    delimiters: ['[[', ']]'],
    el : '#app',
    data : {
        playlist : [],
        videos : null,
        playlink: []
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
                    self.videos = null;
                    self.playlink = [];
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
                    self.videos = data.items;
                    self.playlink = data.playlist;
                    document.body.scrollTop = 0; // For Safari
                    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
                },
                error: function (error_data) {
                    alert("失敗");
                    // console.log(error_data);
                }
            })
        }
    }
});