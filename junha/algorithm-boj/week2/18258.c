#include <stdio.h>
#include <string.h>

int main() {
  int N, x, front = 0, back = -1, data[2000000];
  char command[7];

  scanf("%d", &N);

  for (int i = 0; i < N; i++) {
    scanf("%s", command);

    if (!strcmp(command, "push")) {
      scanf("%d", &x);
      data[++back] = x;
    } else if (!strcmp(command, "pop")) {
      if (front > back)
        printf("-1\n");
      else
        printf("%d\n", data[front++]);
    } else if (!strcmp(command, "size")) {
      printf("%d\n", back - front + 1);
    } else if (!strcmp(command, "empty")) {
      printf("%d\n", front > back);
    } else if (!strcmp(command, "front")) {
      if (front > back)
        printf("-1\n");
      else
        printf("%d\n", data[front]);
    } else {
      if (front > back)
        printf("-1\n");
      else
        printf("%d\n", data[back]);
    }
  }

  return 0;
}