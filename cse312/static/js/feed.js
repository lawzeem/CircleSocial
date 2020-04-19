function addPost(id, username, imgUrl, desc, title){
  console.log("in js file")
  var upvoteURL = String('"/upvote/'+ id +'"');
  var viewURL = String('"/view/'+ id +'"');
  var content = String(
  '<a href='+ viewURL +' class="nav-link">'+
  '<div class="card row col m10 offset-m1 s10 offset-s1">'+
  '<div class="content card-feed">'+
  '<h5>' + username + '</h5>'+
  '<img src="' + imgUrl + '" alt="'+title+'" style="width:100%">'+
  '<br>'+
  '<h5>'+ title +'</h5>'+
  '<h6>'+ desc +'</h6>'+
  '<br>'+
  '</div>'+
  '</div>'+
  '</a>'
  )
  return content;
}
