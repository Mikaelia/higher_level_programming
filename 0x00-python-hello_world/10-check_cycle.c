#include "lists.h"
#include <stdio.h>
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;
	int i;

	slow = list;
	fast = list->next;

	if (list->next ==  NULL)
		return 0;
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
	}
	return (0);
}
