#include "lists.h"
/**
 * check_cycle - check a linked list.
 * @list: listint_t type
 * Return: 1 if there is a cycle or 0 if there isn't cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *pto1, *pto2;

	pto1 = list;
	pto2 = list;
	while (pto1 != NULL && pto2 != NULL && pto2->next != NULL)
	{
		pto2 = pto2->next->next;
		pto1 = pto1->next;
		if (pto2 == pto1)
			return (1);
	}
	return (0);
}
