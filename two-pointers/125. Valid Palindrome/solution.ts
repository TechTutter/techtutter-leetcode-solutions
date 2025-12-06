function isPalindrome(s: string): boolean {
  const parsed = s
    .replace(/[^a-zA-Z0-9]/g, "")
    .toLowerCase()
    .trim();
  const len = parsed.length;
  if (len < 2) return true;
  let i = 0,
    j = len - 1;

  while (i < j) {
    if (parsed[i] !== parsed[j]) return false;
    i++;
    j--;
  }
  return true;
}

export { isPalindrome };
