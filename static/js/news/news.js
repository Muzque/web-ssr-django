// $("button[name='search']").click(function (e) {
//     var search = $(this).parent('div').children('input').val();
//     var endpoint = '/news/api/';
//     $.ajax({
//        method: "GET",
//         url: endpoint,
//         data: {
//            search: search
//         },
//         success: function (data) {
//            // console.log(data);
//             $("table[id='result']").DataTable( {
//                 data: data,
//                 bDestroy: true,
//                 ordering: false,
//                 searching: false,
//                 lengthChange: false,
//                 columns: [
//                     {"data": "link"},
//                     {"data": "title"},
//                     {"data": "description"},
//                     {"data": "author"},
//                     {"data": "publishedAt"},
//                     {"data": "content"}
//                 ],
//                 dom: 'Bfrtip'
//             });
//         },
//         error: function (error_data) {
//             alert("失敗");
//             console.log(error_data);
//         }
//     });
// });

"use strict";

const vm = new Vue({
    delimiters: ['[[', ']]'],
    el : '#app',
    data : {
        news : []
    },
    methods : {
        getNews : function() {
            var self = this;
            var search = document.getElementById("query").value;
            var endpoint = '/news/api/';
            $.ajax({
                method: "GET",
                url: endpoint,
                data: {
                    search: search
                },
                success: function (data) {
                    console.log(data);
                    self.news = data;
                },
                error: function (error_data) {
                    alert("失敗");
                    console.log(error_data);
                }
            });
        }
    }
});