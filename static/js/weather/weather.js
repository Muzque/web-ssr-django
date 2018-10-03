$("button[name='search']").click(function (e) {
    var city = $(this).parent('div').children('input').val();
    var endpoint = '/weather/api/';
    $.ajax({
       method: "GET",
        url: endpoint,
        data: {
           city: city
        },
        success: function (data) {
           // console.log(data);
            $("table[id='result']").DataTable( {
                data: data,
                bDestroy: true,
                ordering: false,
                searching: false,
                lengthChange: false,
                columns: [
                    {"data": "datetime"},
                    {"data": "weather"},
                    {"data": "temp"},
                    {"data": "pressure"},
                    {"data": "humidity"}
                ],
                dom: 'Bfrtip'
            });
        },
        error: function (error_data) {
            alert("失敗");
            console.log(error_data);
        }
    });
});