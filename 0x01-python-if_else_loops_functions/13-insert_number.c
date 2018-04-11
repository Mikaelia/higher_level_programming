#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new;
    listint_t *current;
    listint_t *follow;
    listint_t *temp;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);
    new->n = number;

    if (head == NULL)
        return (NULL);

    current = *head;
    temp = *head;
    follow = *head;

    if (*head == NULL || new->n < current->n)
    {
        new->next = NULL;
        *head = new;
        return (new);
    }

    else
    {
        current = current->next;
        while (new->n > current->n)
        {
            current = current->next;
            follow = follow->next;
            if (current == NULL)
            {
                new->next = current;
                follow->next = new;
                return (temp);
            }
        }
        new->next = current;
        follow->next = new;
    }
    return (temp);
}
