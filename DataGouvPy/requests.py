import io
import pandas as pd

from . import __baseURL__
from .exceptions import DataGouvAPIError
from aiohttp import ClientSession, ContentTypeError, FormData


class DataGouv:
    """
    DataGouv class to handle requests to the data.gouv.fr API.
    """
    def __init__(self, session: ClientSession, __headers__: dict[str, str]) -> None:
        """
        Initialize the DataGouv class.

        :param session: aiohttp ClientSession object
        :param __headers__: Headers to be used in the requests
        """
        self.session = session
        self.__headers__ = __headers__


    async def get_dataset(self, dataset_id: str) -> dict:
        """
        Get a dataset from the data.gouv.fr API.

        :param dataset_id: ID of the dataset to retrieve
        :return: JSON response from the API
        """
        try:
            async with self.session.get(
                url=f"{__baseURL__}/datasets/{dataset_id}/",
                headers=self.__headers__
            ) as response:
                json: dict = await response.json()
                if response.status != 200:
                    raise DataGouvAPIError
                else:
                    return json
        except ContentTypeError:
            raise DataGouvAPIError


    async def upload_dataset_resource(self, dataset_id: str, name: str, data: pd.DataFrame) -> list[dict]:
        """
        Upload a dataset resource to the data.gouv.fr API.

        :param dataset_id: ID of the dataset to upload the resource to
        :param name: Name of the resource file
        :param data: DataFrame to be uploaded as a resource
        :return: JSON response from the API
        """
        csv_buffer = io.StringIO()
        data.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)

        form = FormData()
        form.add_field(
            name="file",
            value=csv_buffer,
            filename=name,
            content_type="application/vnd.ms-excel"
        )
        form.add_field("filename", name)

        try:
            async with self.session.post(
                url=f"{__baseURL__}/datasets/{dataset_id}/upload/", 
                headers=self.__headers__,
                data=form
            ) as response:
                json: list[dict] = await response.json()
                if response.status != 201:
                    raise DataGouvAPIError
                else:
                    return json
        except ContentTypeError:
            raise DataGouvAPIError


    async def update_dataset_resource(self, dataset_id: str, resource_id: str, data: pd.DataFrame, resource_name: str) -> list[dict]:
        """
        Update a dataset resource in the data.gouv.fr API.

        :param dataset_id: ID of the dataset to update the resource in
        :param resource_id: ID of the resource to update
        :param data: DataFrame to be uploaded as a resource
        :param resource_name: Name of the resource file
        :return: JSON response from the API
        """
        csv_buffer = io.StringIO()
        data.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)

        form = FormData()
        form.add_field(
            name="filename",
            value=f"{resource_name}.csv"
        )
        form.add_field(
            name="file",
            value=csv_buffer,
            filename=f"{resource_id}.csv",
            content_type="application/vnd.ms-excel"
        )

        try:
            async with self.session.post(
                url=f"{__baseURL__}/datasets/{dataset_id}/resources/{resource_id}/upload/",
                headers=self.__headers__,
                data=form
            ) as response:
                json: list[dict] = await response.json()
                if response.status != 200:
                    raise DataGouvAPIError
                else:
                    return json
        except ContentTypeError:
            raise DataGouvAPIError


    async def update_dataset_resource_metadata(self, dataset_id: str, resource_id: str, metadata: dict) -> dict:
        """
        Update the metadata of a dataset resource.

        :param dataset_id: ID of the dataset
        :param resource_id: ID of the resource to update
        :param metadata: Metadata to be updated
        :return: JSON response from the API
        """
        try:
            async with self.session.put(
                url=f"{__baseURL__}/datasets/{dataset_id}/resources/{resource_id}/",
                headers=self.__headers__,
                json=metadata
            ) as response:
                json: dict = await response.json()
                if response.status != 200:
                    raise DataGouvAPIError
                else:
                    return json
        except ContentTypeError:
            raise DataGouvAPIError


    async def update_dataset_metadata(self, dataset_id: str, metadata: dict) -> dict:
        """
        Update the metadata of a dataset.

        :param dataset_id: ID of the dataset to update
        :param metadata: Metadata to be updated
        :return: JSON response from the API
        """
        try:
            async with self.session.put(
                url=f"{__baseURL__}/datasets/{dataset_id}/",
                headers=self.__headers__,
                json=metadata
            ) as response:
                json: dict = await response.json()
                if response.status != 200:
                    raise DataGouvAPIError
                else:
                    return json
        except ContentTypeError:
            raise DataGouvAPIError


    async def delete_dataset_resource(self, dataset_id: str, resource_id: str) -> dict:
        """
        Delete a dataset resource.

        :param dataset_id: ID of the dataset
        :param resource_id: ID of the resource to delete
        :return: JSON response from the API
        """
        try:
            async with self.session.delete(
                url=f"{__baseURL__}/datasets/{dataset_id}/resources/{resource_id}/",
                headers=self.__headers__
            ) as response:
                json: dict = await response.json()
                if response.status != 204:
                    raise DataGouvAPIError
                else:
                    return json
        except ContentTypeError:
            raise DataGouvAPIError
