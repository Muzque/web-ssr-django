"use strict";

const vm = new Vue({
    delimiters: ['[[', ']]'],
    el : '#app',
    data : {
        albums : []
    },
    mounted() {
        var self = this;
        var endpoint = '/recommend/api/album/';
        $.getJSON(endpoint, function(data) {
            self.albums = data;
        })
    }
});