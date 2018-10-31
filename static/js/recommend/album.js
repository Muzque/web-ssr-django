"use strict";

const vm = new Vue({
    delimiters: ['[[', ']]'],
    el : '#app',
    data : {
        albums : []
    },
    methods : {
        init: function(){
            this.getItems();
            },
        getItems: function(){
            var endpoint = '/recommend/api/';
            this.$http.get(endpoint)
            .success(function(data){
                this.$set('albums', data);
            })
        }
    }
});