let out = "I wanna be. Let me be? Why I be?! Holly moly..."
    .split(/[\.!?\n]+/)
    .filter((sentance) => sentance.length > 0)
    .map((sentance) => {
        return sentance.trim();
    }

    );
console.log(out);