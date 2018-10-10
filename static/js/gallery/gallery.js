"use strict";

const vm = new Vue({
    delimiters: ['[[', ']]'],
    el : '#app',
    data : {
        gallery : []
    },
    methods : {
        getGallery : function() {
            var self = this;
            var page = document.getElementById("query").value;
            var endpoint = '/gallery/api/';
            $.ajax({
                method: "GET",
                url: endpoint,
                data: {
                    page: page
                },
                success: function (data) {
                    console.log(data);
                    self.gallery = data;
                },
                error: function (error_data) {
                    alert("失敗");
                    // console.log(error_data);
                }
            });
        }
    }
});