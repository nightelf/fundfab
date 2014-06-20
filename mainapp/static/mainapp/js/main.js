angular.module('fundfab', ['ui.bootstrap', 'ui.router']).
    config(function($stateProvider, $urlRouterProvider, $locationProvider) {
    $urlRouterProvider.otherwise("/");
    $stateProvider
      .state('home',{
        url: '/',
        views: {
            'header': {
                template: '<div>header</div>',
                controller: headerCtrl
            },
            'content': {
                templateUrl: '/static/fundfab/templates/home.content.html',
                controller: ListingsCtrl
            },
            'footer': {
                template: '<div>footer</div>',
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

    $scope.title = 'My Custom Title';
}
function footerCtrl($scope) {

    $scope.title = 'My Custom Title';
}