#include "lists.h"

/**
 * is_palindrome - function to call check_pal
 * @head: pointer to the start of the list
 * Return: correct output
 */

int is_palindrome(struct list_head **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (check_pal(head, *head));
}

/**
 * check_pal - function to check if the list is palindrome
 * @head: pointer to the start of the list
 * @last: pointer to the end of the list
 * Return: correct output
 */

int check_pal(listint_t **head, listint_t *last)
{
	if (!last)
		return (1);
	if (check_pal(head, last->next) && (*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
