var request = require('request');
var cheerio = require('cheerio');
var URL = require('url-parse');

var pageUrl = "https://fommshop.com";
var pagePath = "/collections/mens";
var pageSearch = "?page=";
var shirtSize = "Small";
var validPage = true;
var pageNumber = 1;
var maxPageNumber = 10;
var baseUrl = pageUrl + pagePath;

while(validPage){
  var pageUrl = baseUrl + pageSearch + pageNumber ;
  requestBody(pageUrl, function(err, body){
  var mainPage = cheerio.load(body);
  collectInternalProductLinks(mainPage);
  });
  pageNumber++;
  if (pageNumber === maxPageNumber) { validPage = false;}
}

function requestBody(page, callback){
  var options  = {
      uri: page,
      headers: {
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0'
      }
  };
  e = request(options, function(error, response, body) {
      if(error || response.statusCode !== 200) {
          return callback(error || {statusCode: response.statusCode});
      }
      callback(null, body);
   });
}

function searchProducts(page) {
    requestBody(page, function(err, body){
         var sizeFound = searchForWord(body,shirtSize);
         var soldOutFound = searchForWord(body,"Sold Out");
         if(sizeFound && ! soldOutFound){
             console.log(page.replace('?view=quick',''));
             productPage = cheerio.load(body);
             var imgLinks = productPage("img[src^='/']");
             console.log(productPage(imgLinks[0]).attr('src'));
         }
    });
}

function searchForWord(body, word) {
  return(body.indexOf(word) !== -1);
}

function collectInternalProductLinks(page) {
    var relativeLinks = page("a[href^='/']");
    relativeLinks.each(function() {
        if(page(this).attr('href').includes('?view=quick')){
            searchProducts(baseUrl + page(this).attr('href'));
        }
    });
}
