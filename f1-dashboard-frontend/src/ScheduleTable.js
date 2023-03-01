import React, { useMemo, useState, useEffect } from "react";
import Table from './Table';

export function ScheduleTable(props) {
		const [tableData, setTableData] = useState([])

		useEffect(() => {
				fetch('http://localhost:8000/upcoming-table')
						.then(res => res.json())
						.then(data => {
								setTableData(data)
						})
		}, []);

		return
}
