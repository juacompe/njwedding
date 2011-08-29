function test_integration_twitter_feed() {
    // Arrange
    var feed = [];
    // Act
    twitter_search();
    // Assert
    var tweets = $('output div div')
    var msg = "Should be able to fetch tweets"
    jqUnit.ok(tweets.length > 0, msg)
}

