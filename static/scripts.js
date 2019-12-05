    var symps = [];
    var sbox = document.getElementById("sbox");

    $(document).ready(function(){
    $("input").typeahead({
        source: symp_list,
        minLength: 2
        });
     if(!localStorage.getItem("key"))
            {
                introJs().start();
                localStorage.setItem("key", "keyValue");
            };
    });

    function appendNewSymp(name){
        console.log(name);
      symps.push(name.replace("-"," "));
      $("#positive").append(' ' + ' <span class="badge badge-secondary">'+ name +'</span> ' + ' ');
      $('#'+name).remove();
    }
    function deleteSymp(name){
        $('#'+name).remove();
    }
    function appendSymp(){
        var a = $("#symptom").val();
        symps.push(a);
        $("#tags").append('<span> </span><span class="badge badge-secondary">'+a+'</span>')
        $("#symptom").val("");
    }

    $("#symp_upload").click(function(){
      $.ajax({
                url: '/disease',
                type: 'post',
                data: JSON.stringify({
                  'symptoms' : symps
                }),
                dataType: 'JSON',
                contentType: "application/json",
                success: function(response){
                  console.log(response);
                  symps = [];
                  SymFunc(response);
                  console.log("DONE!");
                },
            });
    });

    function sendSymp(){
      $.ajax({
                url: '/find',
                type: 'post',
                data: JSON.stringify({
                  'symptoms' : symps
                }),
                dataType: 'text',
                contentType: "application/json",
                success: function(response){
                  console.log(response);
                  symps = [];
                  showDis(response);
                  console.log("DONE!");
                },
            });
    };

    $("#but_upload").click(function(){

      var fd = new FormData();
      var files = $('#file')[0].files[0];
      if(files == undefined ){
        alert("Please insert an image");
      }
      else {
        fd.append('file',files);
        $("#details").append('<div class="spinner-border" style="width: 3rem; height: 3rem;" role="status"> <span class="sr-only">Loading...</span></div>')
        $.ajax({
            url: '/image',
            type: 'post',
            data: fd,
            contentType: false,
            processData: false,
            success: function(response){
              console.log(response);
              RecieveFunc(response);
            },
        });
      }

    });

    function SymFunc(data){
        $("#cards").empty();
        $("#details").empty();
        $("#slogan").empty();
        sbox.classList.toggle("m-fadeOut");
        if(data.length===0){
            $("#cards").append('<div class="card text-center shadow rounded w-75 center"><div class="card-body"><h5 class="card-title">No results found!</h5></div></div>')
        }
        else{
          $("#details").append('<h3 class="text-white" style="text-align: center; text-shadow: 0 0 20px #000000;"><b>Please answer the following questions.</b></h3><br/><br/><a role="button" aria-pressed="true" href="." class="btn btn-outline-light btn-small">BACK</a>');
          data.forEach(function(name){
            var name = name.replace(/\s/g,'-');;
            $("#cards").append(' <div class="card w-75 center text-center shadow p-3 mb-5 bg-white rounded boxy" id="'+name+'"> <div class="card-body"> <p class="card-title">Do you have/feel ?</p> <h4 class="card-text" style="text-align: center; text-shadow: 0 0 2px #000000;"><b>'+name+'</b></h4> <div class="row"> <div class="col-md-2"></div> <a class="btn btn-outline-success col-md-3 " onclick=appendNewSymp("'+ name +'");><b> YES </b></a> <div class="col-md-2"></div> <a class="btn btn-outline-danger col-md-3" onclick=deleteSymp("'+ name +'");><b> NO </b></a> <div class="col-md-2"></div> </div> </div> </div>');
          })
          $("#cards").append('<div class="card w-75 center text-center shadow p-3 mb-5 bg-white rounded boxy" id="'+name+'"><div class="card-body"><p class="card-title">Your symptoms</p><h5 class="card-text" id="positive"></h5></div><button type="button" onclick=sendSymp(); class="btn btn-warning btn-lg">SEARCH</button></div>');
        };
    };

    function showDis(data){
        $("#cards").empty();
        $("#details").empty();
        $("#details").append('<h1 class="boxy text-white" style="text-align: center; text-shadow: 0 0 20px #000000;"><b>It is most probably '+ data +' .</b></h1><br/><br/><a role="button" aria-pressed="true" href="." class="btn btn-outline-light btn-lg">BACK</a>');
    }
    
    function RecieveFunc(data){
        $("#cards").empty();
        $("#details").empty();
        $("#slogan").empty();
        sbox.classList.toggle("m-fadeOut");
        if(data.length===0){
            $("#cards").append('<div class="card text-center shadow rounded w-75 center"><div class="card-body"><h5 class="card-title">No results found!</h5></div></div><br/><br/><a role="button" aria-pressed="true" href="." class="btn btn-outline-light btn-lg">BACK</a>')
        }
        else{
          $("#details").append('<h3 class="text-white" style="text-align: center; text-shadow: 0 0 20px #000000;"><b>Here is your schedule </b></h3><br/><br/><a role="button" aria-pressed="true" href="." class="btn btn-outline-light btn-small">BACK</a>');
          var count = Object.keys(data).length;
          console.log(count);

          var i = 1;
          // for (;i<=count;i++){
          //   var name = data["T"+i][3];9
          //   var duration = "";
          //   if(i+1<count){
          //       console.log(i, data["T"+(i+1)]);
          //       if(data["T"+(i+1)][0]=="Duration"){
          //           i++;
          //           duration = data["T"+i][3];
          //       }
          //   }
            $("#cards").append('<div class="card w-75 center text-center shadow p-3 mb-5 bg-white rounded boxy"> <div class="card-body"> <h5 class="card-title">Medicine</h5> <p class="card-text">Take Aspirin for 7 days.</p> <a class="btn btn-outline-success">Done</a> </div> </div>');
            $("#cards").append('<div class="card w-75 center text-center shadow p-3 mb-5 bg-white rounded boxy"> <div class="card-body"> <h5 class="card-title">Medicine</h5> <p class="card-text">Take Advil for 3 days.</p> <a class="btn btn-outline-success">Done</a> </div> </div>');
 //         };
          $("#cards").append('<div class="card w-75 center text-center shadow p-3 mb-5 bg-white rounded boxy" id="'+name+'"><div class="card-body"><h3 class="card-title">Syncronize with google ?</h3><h5 class="card-text" id="positive"><button type="button" onclick=sendSymp(); class="btn btn-warning">Add to Google Calender </button></h5></div></div>');
        };
    };
// Google Scripts
 // Client ID and API key from the Developer Console
      var CLIENT_ID = '686668170446-90dc678t33eiobahgan5qte8aod8nq1a.apps.googleusercontent.com';
      var API_KEY = 'AIzaSyBs9ZaCKkEMP7AdJWzDylVKFw_zJ7UzPHE';

      // Array of API discovery doc URLs for APIs used by the quickstart
      var DISCOVERY_DOCS = ["https://www.googleapis.com/discovery/v1/apis/calendar/v3/rest"];
      // secret = "w3cMypYJyHP9rWz3aGVf19MK"
      // Authorization scopes required by the API; multiple scopes can be
      // included, separated by spaces.
      var SCOPES = "https://www.googleapis.com/auth/calendar.readonly";

      var authorizeButton = document.getElementById('authorize_button');
      var signoutButton = document.getElementById('signout_button');

      /**
       *  On load, called to load the auth2 library and API client library.
       */
      function handleClientLoad() {
        gapi.load('client:auth2', initClient);
      }

      /**
       *  Initializes the API client library and sets up sign-in state
       *  listeners.
       */
      function initClient() {
        gapi.client.init({
          apiKey: API_KEY,
          clientId: CLIENT_ID,
          discoveryDocs: DISCOVERY_DOCS,
          scope: SCOPES
        }).then(function () {
          // Listen for sign-in state changes.
          gapi.auth2.getAuthInstance().isSignedIn.listen(updateSigninStatus);

          // Handle the initial sign-in state.
          updateSigninStatus(gapi.auth2.getAuthInstance().isSignedIn.get());
          authorizeButton.onclick = handleAuthClick;
          signoutButton.onclick = handleSignoutClick;
        }, function(error) {
          appendPre(JSON.stringify(error, null, 2));
        });
      }

      /**
       *  Called when the signed in status changes, to update the UI
       *  appropriately. After a sign-in, the API is called.
       */
      function updateSigninStatus(isSignedIn) {
        if (isSignedIn) {
          authorizeButton.style.display = 'none';
          signoutButton.style.display = 'block';
          listUpcomingEvents();
        } else {
          authorizeButton.style.display = 'block';
          signoutButton.style.display = 'none';
        }
      }

      /**
       *  Sign in the user upon button click.
       */
      function handleAuthClick(event) {
        gapi.auth2.getAuthInstance().signIn();
      }

      /**
       *  Sign out the user upon button click.
       */
      function handleSignoutClick(event) {
        gapi.auth2.getAuthInstance().signOut();
      }

      /**
       * Append a pre element to the body containing the given message
       * as its text node. Used to display the results of the API call.
       *
       * @param {string} message Text to be placed in pre element.
       */
      function appendPre(message) {
        var pre = document.getElementById('content');
        var textContent = document.createTextNode(message + '\n');
        pre.appendChild(textContent);
      }

      /**
       * Print the summary and start datetime/date of the next ten events in
       * the authorized user's calendar. If no events are found an
       * appropriate message is printed.
       */
      function listUpcomingEvents() {
        gapi.client.calendar.events.list({
          'calendarId': 'primary',
          'timeMin': (new Date()).toISOString(),
          'showDeleted': false,
          'singleEvents': true,
          'maxResults': 10,
          'orderBy': 'startTime'
        }).then(function(response) {
          var events = response.result.items;
          appendPre('Upcoming events:');

          if (events.length > 0) {
            for (i = 0; i < events.length; i++) {
              var event = events[i];
              var when = event.start.dateTime;
              if (!when) {
                when = event.start.date;
              }
              appendPre(event.summary + ' (' + when + ')')
            }
          } else {
              appendPre('No upcoming events found.');
          }
        });
      }