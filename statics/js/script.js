var test = angular.module("test", [], function ($interpolateProvider) {
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");
});

test.controller('MainCtrl', [ '$scope', '$http', '$interval', function($scope, $http, $interval) {
	$scope.myname = 'Test';
	$interval(function(){
		$http.get('/latest-user/json/')
		.success(function(data, status, headers, config) {
	      	console.log(data[0].name);
	      	$scope.myname = data[0].name;
	      	// $scope.$apply();
	    });
	}, 5000, 0)

}]);