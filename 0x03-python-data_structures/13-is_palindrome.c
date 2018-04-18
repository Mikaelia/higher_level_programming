#include "lists.h"
#include "stdio.h"
/**
  * findlen - finds len of list
  * @head: pointer to head
  *
  * Return: length of list
  */
int findlen(listint_t *head)
{
	int len;

	len = 0;
	while (head)
	{
		head = head->next;
		len++;
	}
	return (len);
}
/**
  * is_palindrome - checks to see if linked list is a palendrome
  * @head: pointer to head
  *
  * Return: 0 if not palindrome, 1 if palindrome
  */
int is_palindrome(listint_t **head)
{
	listint_t *slow;
	listint_t *fast;
	int len, half, x, y;

	if (*head == NULL)
	{
		return (1);
	}
	if ((*head)->next == NULL)
	{
		return (1);
	}
	slow = *head;
	fast = *head;
	len = findlen(*head);
	if (len == 0)
	{
		return (1);
	}
	x = 0;
	y = 0;
	half = len / 2;
	while (x < half)
	{
		while (y < len - 1)
		{
			fast = fast->next;
			y++;
		}
		if (slow->n != fast->n)
		{
			return (0);
		}
		len--;
		slow = slow->next;
		fast = *head;
		x++;
		y = 0;
	}
	return (1);
}
