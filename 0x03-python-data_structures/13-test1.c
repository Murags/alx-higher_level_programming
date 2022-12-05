#include "lists.h"
/**
*is_palindrome - checks if a list is palindrome
*
*@head: pointer to list
*
*Return: 1 if palindrome else 0
*/
int is_palindrome(listint_t **head)
{
	int i = 0, j, temp;
	listint_t *current, *new = NULL, *curr2;

	current = *head;
	while (current)
	{
		add_nodeint_end(&new, current->n);
		i++;
		current = current->next;
	}
	i--;
	while (i > 0)
	{
		current = new;
		j = 0;
		while (j < i && current->next)
		{
			temp = current->n;
			current->n = current->next->n;
			current->next->n = temp;
			current = current->next;
			j++;
		}
		i--;
	}
	current = *head;
	curr2 = new;
	while (current)
	{
		if (curr2->n != current->n)
		{
			free_listint(new);
			return (0);
		}
		current = current->next;
		curr2 = curr2->next;
	}
	free_listint(new);
	return (1);
}
