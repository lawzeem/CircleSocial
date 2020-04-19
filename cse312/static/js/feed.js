function addPost(id, username, imgUrl, desc){
  console.log("in js file")
  var upvoteURL = String('"/upvote/'+ id +'"');
  var viewURL = String('"/view/'+ id +'"');
  var content = String('<div class="card row col m10 offset-m1 s10 offset-s1">'+
  '<div class="content card-feed">'+
  '<h5>' + username + '</h5>'+
  '<img src="' + imgUrl + '" alt="dog" style="width:100%">'+
  '<br>'+
  '<h6>'+ desc +'</h6>'+
  '<br>'+
  '<div class="row">'+
  '<a href='+ upvoteURL +' class="col l1 s6 btn-large waves-effect waves-light blue"><i class="material-icons ">thumb_up</i></a>'+
  '<a href='+ viewURL +' class="col l1 s6 btn-large waves-effect waves-light blue"><i class="material-icons ">comment</i></a>'+
  '</div>'+
  '</div>'+
  '</div>')
  return content;
}
