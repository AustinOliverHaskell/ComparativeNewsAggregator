// Scrape Keywords

const numberOfTiles = 30;
const columns = 6;
const rows = 8;
var rowValue = 1;

const REDIRECT_PAGE = "article.html";
const ERROR_PAGE    = "error.html";

var keywords = [];

var colors = ["#8d99ae","#f29559", "#605b56", "#ffffff"];

function scrapeKeywords()
{
	var database = firebase.database();


	firebase.database().ref('Keybois').once('value').then(function(snapshot)
	{
		snapshot.forEach(function (childSnapshot)
		{
            var value = childSnapshot.val();
            keywords.push(value);
        });

        if (keywords.length > 0)
        {
			oCreateTiles();
		}
		else
		{
			window.location = ERROR_PAGE;
		}
	});
}

function oCreateTiles()
{
	var id = 0;
	for (var i = 0; i < rows; i++)
	{
		$("#tiles").append(startRow());
		for (var q = 0; q < columns; q++)
		{
			var colorScheme = Math.floor(Math.random()*3)

			if (id < keywords.length)
			{

				// Figure out if we need to make a double tile
				var join = Math.floor(Math.random() * 10);
				if (join === 5)
				{
					$("#tiles").append(initTile(id, 4, keywords[id]));

					$("#"+id+"").css("background-color", colors[colorScheme]);

					// Add the function to select a cookie
					$("#"+id).click(function() {
						selectCookie($(this).text());
					});

					if (colorScheme === 2)
					{
						$("#"+id+"").css("color", colors[3]);
					}

					for (; q < columns-2; q++)
					{
						// Duplicate code, me so sorry
						$("#tiles").append(initTile(id, 2, keywords[id]));

						$("#"+id+"").css("background-color", colors[colorScheme]);

						// Add the function to select a cookie
						$("#"+id).click(function() {
							selectCookie($(this).text());
						});

						if (colorScheme === 2)
						{
							$("#"+id+"").css("color", colors[3]);
						}

						id++;
					}
					break;
				}
			
				$("#tiles").append(initTile(id, 2, keywords[id]));

				$("#"+id+"").css("background-color", colors[colorScheme]);

				// Add the function to select a cookie
				$("#"+id).click(function() {
					selectCookie($(this).text());
				});

				if (colorScheme === 2)
				{
					$("#"+id+"").css("color", colors[3]);
				}

			}

			id++;
		}
		$("#tiles").append(endRow());
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

function startRow()
{
	return "<div class='row'>";
}

function endRow()
{
	return "</div>";
}

function selectCookie(keyword)
{
	console.log(keyword + " saved to cookie");
	document.cookie = keyword;
	window.location = REDIRECT_PAGE;
}
