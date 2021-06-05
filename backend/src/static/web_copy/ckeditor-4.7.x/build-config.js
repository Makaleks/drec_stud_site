/**
 * @license Copyright (c) 2003-2017, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.md or http://ckeditor.com/license
 */

/* exported CKBUILDER_CONFIG */

var CKBUILDER_CONFIG = {
	skin: 'moono-lisa',
	ignore: [
		'bender.js',
		'bender.ci.js',
		'.bender',
		'bender-err.log',
		'bender-out.log',
		'.travis.yml',
		'dev',
		'docs',
		'.DS_Store',
		'.editorconfig',
		'.gitignore',
		'.gitattributes',
		'gruntfile.js',
		'.idea',
		'.jscsrc',
		'.jshintignore',
		'.jshintrc',
		'less',
		'.mailmap',
		'node_modules',
		'package.json',
		'README.md',
		'tests'
	],
	plugins: {
		a11yhelp: 1,
		about: 1,
		basicstyles: 1,
		bbcode: 1,
//		bidi: 1,
		blockquote: 1,
		clipboard: 1,
//		codesnippet: 1,
		colorbutton: 1,
		colordialog: 1,
		copyformatting: 1,
		contextmenu: 1,
//		dialogadvtab: 1,
//		div: 1,
//		elementspath: 1,
		enterkey: 1,
		entities: 1,
//		filebrowser: 1,
		find: 1,
//		flash: 1,
//		floatingspace: 1,
//		font: 1,
// Unsupported by bbcode plugin
//		format: 1,
//		forms: 1,
//		horizontalrule: 1,
// Should be turned off in most cases
//		htmlwriter: 1,
//		iframe: 1,
		image: 1,
		indentlist: 1,
//		indentblock: 1,
// Unsupported by bbcode plugin
//		justify: 1,
// WCAG
//		language: 1,
		link: 1,
		list: 1,
		liststyle: 1,
		magicline: 1,
		maximize: 1,
//		newpage: 1,
// Printing
//		pagebreak: 1,
// Unsupported by bbcode plugin
//		pastefromword: 1,
//		pastetext: 1,
//		preview: 1,
//		print: 1,
		removeformat: 1,
//		resize: 1,
//		save: 1,
//		selectall: 1,
//		showblocks: 1,
// Unsupported by bbcode plugin
//		showborders: 1,
//		smiley: 1,
//		sourcearea: 1,
		specialchar: 1,
//		stylescombo: 1,
		tab: 1,
// Unsupported by bbcode plugin
//		table: 1,
//		tableselection: 1,
//		tabletools: 1,
//		templates: 1,
		toolbar: 1,
		undo: 1,
		wysiwygarea: 1
	}
};
