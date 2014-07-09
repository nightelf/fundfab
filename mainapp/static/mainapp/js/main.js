var fundfab = angular.module('fundfab', ['ui.bootstrap', 'ui.router']).
    config(function($stateProvider, $urlRouterProvider, $locationProvider) {
    $urlRouterProvider
        .when('', '/')
        .otherwise("/");
    $stateProvider
      .state('home',{
        url: '/',
        views: {
            'contextMenu': {
                templateUrl: '/static/fundfab/templates/home.context.html',
                controller: function($scope) {

                }
            },
            'content': {
                templateUrl: '/static/fundfab/templates/home.content.html',
                controller: ListingsCtrl
            },
        }
    })
      .state('signin',{
        url: '/signin',
        views: {
            'contextMenu': {
                templateUrl: '/static/fundfab/templates/home.context.html',
                controller: function($scope) {

                }
            },
            'content': {
                templateUrl: '/static/fundfab/templates/home.signin.html',
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
    $scope.toggled = function(open) {
        console.log('Dropdown is now: ', open);
    };
    $scope.toggleDropdown = function($event) {
        $event.preventDefault();
        $event.stopPropagation();
        $scope.status.isopen = !$scope.status.isopen;
    };
}]);

fundfab.controller('footerCtrl', ['$scope', function($scope) {

    $scope.title = 'My Custom footer';
}]);