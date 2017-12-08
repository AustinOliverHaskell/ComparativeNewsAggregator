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

	// When the keywords have been populated
	// create the tiles
	createTiles();
}

function createTiles()
{
	var id = 0;
	for (var i = 0; i < rows; i++)
	{
		var completeRow = 10;

		$("#tiles").append(addSpace());
		while(completeRow > 0)
		{
			if (keywords.length <= id)
			{
				//break;
			}

			var value = Math.floor((Math.random() * 2) + 1);

			completeRow -= value+1;

			var colorScheme = Math.floor(Math.random()*4)

			$("#tiles").append(initTile(id, value, "Untitled"));
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

			id++;
		}
		$("#tiles").append(addSpace());
	}
}

function initTile(pos, size, key)
{

	return "<div class='tile col-xs-"+size+"' id='"+pos+"'>"+key+pos+"</div>";
}

function addSpace()
{
	return "<div class='tile col-xs-1'> </div>";
}

function selectCookie(keyword)
{
	document.cookie = keyword;
}
