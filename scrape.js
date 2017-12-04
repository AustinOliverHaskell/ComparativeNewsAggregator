// Scrape Keywords

const numberOfTiles = 30;
const columns = 5;
const rows = 4;
var rowValue = 1;

function scrapeKeywords()
{
	console.log("Hello");
}

function createTiles()
{
	for (var i = 0; i < rows; i++)
	{
		var completeRow = 12;

		for (var q = 0; q < columns; q++)
		{
			var value = Math.floor((Math.random() * completeRow) + 1);

			completeRow -= value;

			$("#tiles").append(initTile(i, value));
		}
	}
}

function initTile(pos, size)
{

	return "<div class='tile col-xs-"+size+" id='"+ pos +"'>Hello</div>";
}