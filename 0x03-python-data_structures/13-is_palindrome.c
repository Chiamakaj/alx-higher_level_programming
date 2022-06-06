#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - a function in C that checks if a
 * singly linked list is a palindrome.
 * @head: head of node
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	unsigned int dis = 1;
	listint_t *tmp;

	if (head == NULL)
		return (1);
	tmp = *head;
	while (tmp) /* get length of list */
	{
		tmp = tmp->next;
		dis++;
	}
	return (0);
}
