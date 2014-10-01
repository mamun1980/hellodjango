var test = angular.module("test", [], function ($interpolateProvider) {
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");
});

test.controller('MainCtrl', [ '$scope', '$http', '$interval', function($scope, $http, $interval) {
	$scope.init = function() {
		$http.get('/latest-user/json/')
		.success(function(data, status, headers, config) {

	      	$scope.hellos = data;
	    });
	};
	$scope.init();
	$interval(function(){
		$http.get('/latest-user/json/')
		.success(function(data, status, headers, config) {

	      	$scope.hellos = data;
	    });
	}, 5000, 0)

}]);