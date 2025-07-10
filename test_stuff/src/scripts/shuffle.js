export function shuffle(array) {
  const shuffledArray = [...array];
  let currentIndex = shuffledArray.length;

  const crypto = window.crypto || window.msCrypto; 
  
  while (currentIndex !== 0) {
    const randomBytes = new Uint32Array(1);
    crypto.getRandomValues(randomBytes);
    const randomIndex = randomBytes[0] % currentIndex;
    
    currentIndex--;
    [shuffledArray[currentIndex], shuffledArray[randomIndex]] = 
      [shuffledArray[randomIndex], shuffledArray[currentIndex]];
  }

  return shuffledArray;
}
