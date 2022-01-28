#include "hash_tables.h"
/**
 * hash_table_create - create a hash table
 *
 * @size: size of the hash table
 * Return: New hash table
 */

hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *new_hashTable;

	if (size == 0)
		return (NULL);

	new_hashTable = malloc(sizeof(hash_table_t));
	if (!new_hashTable)
		return (NULL);

	new_hashTable->size = size;

	new_hashTable->array = malloc(sizeof(hash_node_t *) * size);
	if (!new_hashTable->array)
		return (NULL);

	return (new_hashTable);
}