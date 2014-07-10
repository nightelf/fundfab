var fundfab = angular.module('fundfab', ['ngCookies', 'ui.bootstrap', 'ui.router']).
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
                controller: function($scope, $http) {

                    $scope.login = {};
                    $scope.login.email = '';
                    $scope.login.password = '';
                    $scope.login.url = '/auth/login-email-submit';
                    $scope.login.method = 'post';
                    $scope.login.disabled = false;

                    // login submit
                    $scope.loginSubmit = function() {
                        $scope.login.disabled = true;
                        $scope.code = null;
                        $scope.response = null;
                        postData = {
                            email: $scope.login.email,
                            password: $scope.login.password,
                        };

                        $http({data: postData, method: $scope.login.method, url: $scope.login.url, cache: false}).
                        success(function(data, status) {
                            $scope.login.disabled = false;
                            console.log('there was a success');
                        }).
                        error(function(data, status) {
                            $scope.disabled = false;
                            console.log('there was an error');
                        })
                    }
                }
            },
        }
    });
    // @todo html5mode $locationProvider.html5mode(true);
}).run(function($http, $cookies) {
    $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
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