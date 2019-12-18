#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * *is_pal - function to recursively check values of head and tail.
 * @head: double pointer of listint_t type to head.
 * @tail: single pointer of listint_t type to tail.
 * Return: 1 if palidrome.
 */
int is_pal(listint_t **head, listint_t *tail)
{
	if (tail == NULL)
		return (1);
	if (is_pal(head, tail->next) && (*head)->n == tail->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - function to check if singly linked list is a palidrome
 * @head: double pointer of listint_t type to head.
 * Return: 0 if not palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)

	return (is_pal(head, *head));
}
