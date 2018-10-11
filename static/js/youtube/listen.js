const vm2 = new Vue({
    delimiters: ['[[', ']]'],
    el : '#app',
    data : {
        videos : []
    },
    methods : {
        getListen : function(e) {
            e = e || window.event;
            e = e.target || e.srcElement;
            var playlistId = e.id;
            var endpoint = '/youtube/api/listen/';
            $.ajax({
                method: "GET",
                url: endpoint,
                data: {
                    playlistId: playlistId
                },
                success: function (data) {
                    console.log(data);
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