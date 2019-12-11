#include "lists.h"

/**
 * insert_node - function to insert node.
 * @head: double pointer of listint_t type.
 * @number: int type.
 * Return: address of new node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nd, *t;

	nd = malloc(sizeof(listint_t));
	if (nd == NULL)
		return (NULL);
	nd->nd = number;
	nd->next = NULL;

	if (*head == NULL)
	{
		*head = nd;
		nd->next = NULL;
		return (nd);
	}

	t = *head;
	while (t->next != NULL)
	{
		if (number < t->n)
		{
			nd->next = t;
			*head = nd;
			return (nd);
		}
		if (number <= t->next->n)
		{
			nd->next = temp->next;
			t->next = nd;
			return (nd);
		}
	t = t->next;
	}
	nd->next = NULL;
	t->next = nd;
	return (nd);
}
