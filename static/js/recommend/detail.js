"use strict";

const vm = new Vue({
    delimiters: ['[[', ']]'],
    el : '#app',
    data : {
        songs : []
    },
    mounted() {
        var self = this;
        var url = new URL(window.location.href);
        var pk = url.searchParams.get("pk");
        console.log(pk);
        var endpoint = '/recommend/api/songs/' + pk;
        $.getJSON(endpoint, function(data) {
            self.songs = data;
        })
    }
});
