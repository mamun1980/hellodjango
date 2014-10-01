var test = angular.module("test", [], function ($interpolateProvider) {
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");
});

test.controller('MainCtrl', [ '$scope', '$http', '$interval', function($scope, $http, $interval) {
	$scope.myname = 'Test';
	$interval(function(){
		$http.get('/latest-user/json/')
		.success(function(data, status, headers, config) {

	      	$scope.hellos = data;
	    });
	}, 20000, 0)

}]);