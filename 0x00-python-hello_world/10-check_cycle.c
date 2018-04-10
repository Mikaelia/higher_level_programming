#include "lists.h"
#include <stdio.h>
/**
  * check_cycle - checks linked list for cycle
  * list: list head
  *
  * Return: 0 for no cycle, 1 for cycle
  */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;
	int i;

	if (list == NULL)
		return (0);
	if (list->next == NULL)
		return (0);
	slow = list;
	fast = list->next;

	while (fast != NULL  && slow != NULL)
	{
		if (slow == fast)
			return (1);
		i = 0;
		while (i < 2 && fast->next != NULL)
		{
			fast = fast->next;
			if (fast->next == NULL)
				return (0);
			i++;
		}
		slow = slow->next;
		if (slow->next == NULL)
			return (0);
	}
	return (0);
}
