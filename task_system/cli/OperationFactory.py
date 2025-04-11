from task_system.cli.CreateTaskOperation import CreateTaskOperation
from task_system.cli.DeleteTaskOperation import DeleteTaskOperation
from task_system.cli.ListTasksOperation import ListTasksOperation
from task_system.cli.Operation import Operation
from task_system.cli.OperationStrategy import OperationStrategy
from task_system.cli.TaskClientInterface import TaskClientInterface
from task_system.cli.UpdateTaskOperation import UpdateTaskOperation
from task_system.cli.ViewTaskOperation import ViewTaskOperation


class OperationFactory:
    @staticmethod
    def create_operation(operation: Operation, client: TaskClientInterface) -> OperationStrategy:
        operations = {
            Operation.CREATE: CreateTaskOperation(client),
            Operation.READ: ViewTaskOperation(client),
            Operation.UPDATE: UpdateTaskOperation(client),
            Operation.DELETE: DeleteTaskOperation(client),
            Operation.LIST: ListTasksOperation(client)
        }
        return operations.get(operation)