// Scrape Keywords

const numberOfTiles = 30;
const columns = 5;
const rows = 3;
var rowValue = 1;

var keywords = [];

var colors = ["#8d99ae","#f29559", "#605b56", "#ffffff"];

function scrapeKeywords()
{
	var database = firebase.database();


	firebase.database().ref('Keybois').once('value').then(function(snapshot){

		snapshot.forEach(function (childSnapshot) {

            var value = childSnapshot.val();
            keywords.push(value);
        });
		oCreateTiles();
	});

	// When the keywords have been populated
	// create the tiles
}

/*function createTiles()
{
	var id = 0;
	for (var i = 0; i < rows; i++)
	{
		var completeRow = 10;

		$("#tiles").append(addSpace());
		$("#tiles").append(addSpace());
		while(completeRow > 0)
		{
			if (keywords.length <= id)
			{
				//break;
			}

			var value = 4;

			completeRow -= value+2;

			var colorScheme = Math.floor(Math.random()*4)

			$("#tiles").append(initTile(id, value, "Untitled"));

			$("#"+id+"").css("background-color", colors[colorScheme]);

			// Add the function to select a cookie
			$("#"+id).click(function() {
				selectCookie($(this).text());
			});

			if (colorScheme === 3)
			{
				$("#"+id+"").css("color", colors[2]);
			}

			id++;
		}
	}
}*/

function oCreateTiles()
{
	var id = 0;
	for (var i = 0; i < rows; i++)
	{
		for (var q = 0; q < columns; q++)
		{
			var colorScheme = Math.floor(Math.random()*4)

			if (id < keywords.length)
			{
				$("#tiles").append(addSpace());
				$("#tiles").append(initTile(id, 4, keywords[id]));
				$("#tiles").append(addSpace());

				$("#"+id+"").css("background-color", colors[colorScheme]);

				// Add the function to select a cookie
				$("#"+id).click(function() {
					selectCookie($(this).text());
				});

				if (colorScheme === 3)
				{
					$("#"+id+"").css("color", colors[2]);
				}
			}

			id++;
		}
	}
}

function initTile(pos, size, key)
{

	return "<div class='tile col-xs-"+size+"' id='"+pos+"'>"+key+"</div>";
}

function addSpace()
{
	return "<div class='tile col-xs-1'> </div>";
}

function selectCookie(keyword)
{
	console.log(keyword + " saved to cookie");
	document.cookie = keyword;
}
