var mots=[];
d3.text("mots.txt", function(txt) {
	txt.split("\n").forEach(function(line) {
		mot=line.split("\t");
		
		var stemW=mot[1].split(" ");
		stemW=stemW.map(stemmer);
		
		mots.push({critere:mot[0],mots:stemW});
	});
});

var PT=[];
var rows=["category","account","date","text","id_str"];
d3.text("politweets.txt", function(txt) {
	txt.split("\n").forEach(function(l) {
		var tweet={};
		l.split("\t").forEach(function(c,i) {tweet[rows[i]]=c;});
		var score={};
		var textS=tidy(tweet.text);
		textS=textS.split(" ");
		textS=textS.map(stemmer);
		var wordsInTweets=textS.length;	
		textS.forEach(function(s,i) {
				mots.forEach(function(m) {
					var l=m.mots.length;
					if (!score[m.critere]) {score[m.critere]=0;}
					if(l+i<wordsInTweets){
					
						// this is an obsfuscated formula. what it does is: 
						// from the i-th stemmed word in the textS array, 
						// check that each of the next l words is similar to the l words of 
						// the scoring word, m.mots (also an array). 
						// if this is true, then 1 (~~true) is added to the score of this tweet
						// for the relevant criteria (from m.critere).
					
						score[m.critere]+=~~(d3.range(l).every(function(j) {return textS[i+j]==m.mots[j];}));
					}
				});
			});
		tweet["score"]=score;
		var myDateObj=new Date(tweet.date);
		tweet["day"]=myDateObj.getFullYear()+"-"+(myDateObj.getMonth()+1)+"-"+myDateObj.getDate();

		PT.push(tweet);
		
	})
});


