"use strict";

const vm = new Vue({
    delimiters: ['[[', ']]'],
    el : '#app',
    data : {
        album : []
    },
    methods : {
        init: function(){
            this.getItems();
            },
        getItems: function(){
            var endpoint = '/recommend/api/';
            this.$http.get(endpoint)
            .success(function(data){
                this.$set('album', data);
            })
        }
    }
});