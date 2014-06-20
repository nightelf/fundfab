angular.module('fundfab', ['ui.bootstrap', 'ui.router']).
    config(function($stateProvider, $urlRouterProvider, $locationProvider) {
    $urlRouterProvider
        .when('', '/')
        .otherwise("/");
    $stateProvider
      .state('home',{
        url: '/',
        views: {
            'header': {
                templateUrl: '/static/fundfab/templates/home.header.html',
                controller: headerCtrl
            },
            'content': {
                templateUrl: '/static/fundfab/templates/home.content.html',
                controller: ListingsCtrl
            },
            'footer': {
                templateUrl: '/static/fundfab/templates/home.footer.html',
                controller: footerCtrl
            },
        }
    });
    // @todo html5mode $locationProvider.html5mode(true);
});

function ListingsCtrl($scope) {

    $scope.title = 'My Custom Title';
}
function headerCtrl($scope) {

    $scope.title = 'My Custom header';
}
function footerCtrl($scope) {

    $scope.title = 'My Custom footer';
}