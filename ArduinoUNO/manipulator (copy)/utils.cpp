bool checkRange(int n, int start=0, int end=180) {
  return start <= n && n <= end;
}

int clipRange(int n, int start=0, int end=180) {
  if (start > n)
    return start;
  if (end < n)
    return end;
  return n;
}
