import asyncio
import pandas as pd

from . import __headers__
from .requests import DataGouv as DataGouvRequests
from .exceptions import DataGouvAPIError
from async_timeout import timeout
from aiohttp import ClientSession


timeout_time = 30


class DataGouv:
    """
    DataGouv class to handle requests to the data.gouv.fr API.
    """
    def __init__(self, session: ClientSession, api_key: str) -> None:
        """
        Initialize the DataGouv class.

        :param session: aiohttp ClientSession object
        :param api_key: API key for authentication
        """
        self.client = DataGouvRequests(
            session=session, 
            __headers__={
                "X-API-KEY": api_key,
                **__headers__
            }
        )

        self.datasets = Datasets(self.client)


class Datasets:
    """
    Datasets class to handle requests to the data.gouv.fr API for datasets.
    """
    def __init__(self, client: DataGouvRequests) -> None:
        """
        Initialize the Datasets class.

        :param client: DataGouvRequests object
        """
        self.client = client


    async def get_dataset(self, dataset_id: str) -> dict:
        """
        Get a dataset from the data.gouv.fr API.

        :param dataset_id: ID of the dataset to retrieve
        :return: JSON response from the API
        """
        try:
            async with timeout(timeout_time):
                return await self.client.get_dataset(dataset_id=dataset_id)
        except asyncio.TimeoutError:
            raise DataGouvAPIError


    async def upload_resource(
        self, 
        dataset_id: str, 
        dataset: pd.DataFrame, 
        resource_name: str, 
        resource_description: str, 
    ) -> list[dict]:
        """
        Upload a dataset resource to the data.gouv.fr API.

        :param dataset_id: ID of the dataset to upload the resource to
        :param dataset: DataFrame to be uploaded as a resource
        :param resource_name: Name of the resource file
        :param resource_description: Description of the resource
        :return: JSON response from the API
        """
        try:
            async with timeout(timeout_time):
                d = await self.client.upload_dataset_resource(
                    dataset_id=dataset_id, 
                    name=resource_name,
                    data=dataset
                )

                await self.client.update_dataset_resource_metadata(
                    dataset_id=dataset_id, 
                    resource_id=d["id"], 
                    metadata={
                        "description": resource_description,
                        "filetype": "file",
                        "schema": None,
                        "title": resource_name,
                        "type": "main"
                    }
                )
        except asyncio.TimeoutError:
            raise DataGouvAPIError


    async def update_dataset_resource(
        self, 
        dataset_id: str, 
        resource_id: str, 
        dataset: pd.DataFrame, 
        resource_name: str, 
        resource_description: str,
    ) -> list[dict]:
        """
        Update a dataset resource in the data.gouv.fr API.

        :param dataset_id: ID of the dataset
        :param resource_id: ID of the resource to update
        :param dataset: DataFrame to be uploaded as a resource
        :param resource_name: Name of the resource file
        :param resource_description: Description of the resource
        :return: JSON response from the API
        """
        try:
            async with timeout(timeout_time):
                d = await self.client.update_dataset_resource(
                    dataset_id=dataset_id, 
                    resource_id=resource_id,
                    data=dataset
                )

                await self.client.update_dataset_resource_metadata(
                    dataset_id=dataset_id, 
                    resource_id=d["id"], 
                    metadata={
                        "description": resource_description,
                        "filetype": "file",
                        "schema": None,
                        "title": resource_name,
                        "type": "main"
                    }
                )
        except asyncio.TimeoutError:
            raise DataGouvAPIError


    async def update_dataset_metadata(
        self, 
        dataset_id: str, 
        metadata: dict
    ) -> dict:
        """
        Update the metadata of a dataset resource.

        :param dataset_id: ID of the dataset
        :param metadata: Metadata to be updated
        :return: JSON response from the API
        """
        try:
            async with timeout(timeout_time):
                return await self.client.update_dataset_metadata(
                    dataset_id=dataset_id, 
                    metadata=metadata
                )
        except asyncio.TimeoutError:
            raise DataGouvAPIError


    async def delete_resource(self, dataset_id: str, resource_id: str) -> dict:
        """
        Delete a dataset resource from the data.gouv.fr API.

        :param dataset_id: ID of the dataset
        :param resource_id: ID of the resource to delete
        :return: JSON response from the API
        """
        try:
            async with timeout(timeout_time):
                return await self.client.delete_dataset_resource(
                    dataset_id=dataset_id, 
                    resource_id=resource_id
                )
        except asyncio.TimeoutError:
            raise DataGouvAPIError
