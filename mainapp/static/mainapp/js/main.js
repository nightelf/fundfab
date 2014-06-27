var fundfab = angular.module('fundfab', ['ui.bootstrap', 'ui.router']).
    config(function($stateProvider, $urlRouterProvider, $locationProvider) {
    $urlRouterProvider
        .when('', '/')
        .otherwise("/");
    $stateProvider
      .state('home',{
        url: '/',
        views: {
            'content': {
                templateUrl: '/static/fundfab/templates/home.content.html',
                controller: ListingsCtrl
            },
        }
    });
    // @todo html5mode $locationProvider.html5mode(true);
});


function ListingsCtrl($scope) {

    $scope.title = 'My Custom Title';
}

fundfab.controller('headerCtrl', ['$scope', function($scope) {
    $scope.title = 'My Custom header';
}]);

fundfab.controller('footerCtrl', ['$scope', function($scope) {

    $scope.title = 'My Custom footer';
}]);