#include "lists.h"
int recursepalindrome(listint_t **left, listint_t *right)
{
	int match;

	if (right == NULL)
		return (1);
	match = recursepalindrome(left, right->next);
	if (match == 0)
		return (0);
	if ((*left)->n == right->n)
	{
		*left = (*left)->next;
		return(1);
	}
	else
		return (0);
}

